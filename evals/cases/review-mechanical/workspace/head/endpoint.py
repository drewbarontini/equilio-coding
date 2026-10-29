def release_response(release):
    return {"status": 200, "body": release,
            "headers": {"Cache-Control": "public, max-age=60"}}
