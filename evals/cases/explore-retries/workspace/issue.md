# Recover notifications after timeouts

The current sender stops on a provider timeout and has no retry path. Compare an immediate retry with a deferred queue so notifications can recover without duplicate delivery.

We do not yet know the real provider's deduplication contract.
