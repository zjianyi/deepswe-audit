"""Archive expansion S0 raw output without changing BTQC's reviewer or validation."""
import os
import shutil
from datetime import datetime, timezone
from audit_core import write, sha


def run_once(out, review_function):
    from btqc.semantic.codex import CodexCliReviewer, SemanticInfrastructureError
    # Exclusive durable marker prevents a crashed attempt from being silently repeated.
    marker=out/'attempt.json'
    if marker.exists():
        raise RuntimeError('S0 attempt already started; inspect retained evidence, never relaunch automatically')
    write(marker,{'sequence':'S0','started_at':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'input_sha256':sha(out/'input.json')})
    class ArchivingReviewer(CodexCliReviewer):
        def review(self,bundle,schema_path,output_path):
            shutil.copytree(bundle,out/'bundle')
            try:
                return super().review(bundle,schema_path,output_path)
            finally:
                if output_path.exists():shutil.copy2(output_path,out/'raw-review.json')
    try:
        backend=ArchivingReviewer(out.resolve())
        return review_function(out/'input.json',ledger_path=out/'ledger.json',backend=backend)
    except SemanticInfrastructureError as exc:
        return {'schema_version':'btqc.semantic-review-run/1','phase':'semantic','overall_status':'INFRASTRUCTURE_FAILURE','error':{'code':exc.code,'message':exc.message,'evidence':exc.evidence}}
