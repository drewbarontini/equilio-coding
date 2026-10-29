from endpoint import release_response


def public_release(version):
    return release_response({"version": version, "channel": "stable"})
