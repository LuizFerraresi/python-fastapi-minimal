
async def whoami(request_client: str, request_headers: dict[str, str]):
    header_forwarded_for = request_headers.get("x-forwarded-for")
    ip = header_forwarded_for.split(',')[0].strip() if header_forwarded_for else request_client

    return {
        "ip": ip,
        "client": request_client,
        "user_agent": request_headers.get("user-agent", "unknown"),
        "headers": dict(request_headers),
    }
