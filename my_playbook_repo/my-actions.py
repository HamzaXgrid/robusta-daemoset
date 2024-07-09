from hikaru.model.rel_1_26 import DaemonSet
from robusta.api import (
    DaemonSetEvent,
    action,
    does_daemonset_have_toleration,
)

@action
def daemonset_status_enricher(event: DaemonSetEvent):
    """
    Enrich the finding with daemon set stats.

    Includes recommendations for the identified cause.
    """
    ds: DaemonSet = event.get_daemonset()
    print("Daemonsets",ds)
    # Define the tolerations to be added
    # new_tolerations = [
    #     {
    #         "key": "key1",
    #         "operator": "Equal",
    #         "value": "value1",
    #         "effect": "NoSchedule"
    #     },
    #     {
    #         "key": "key2",
    #         "operator": "Exists",
    #         "effect": "NoExecute",
    #         "tolerationSeconds": 3600
    #     }
    # ]
    
    # # Add tolerations if they do not already exist
    # if not does_daemonset_have_toleration(ds, new_tolerations):
    #     if not ds.spec.template.spec.tolerations:
    #         ds.spec.template.spec.tolerations = new_tolerations
    #     else:
    #         for toleration in new_tolerations:
    #             if toleration not in ds.spec.template.spec.tolerations:
    #                 ds.spec.template.spec.tolerations.append(toleration)
    
    # # Update the DaemonSet with the new tolerations
    # ds.update()

