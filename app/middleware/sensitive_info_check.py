class SensitiveInfoCheck:
    async def process(self, request, call_next):
        # Assume check_for_sensitive_info is a function that returns True if
        # sensitive info is found in the request.
        if check_for_sensitive_info(request):
            return JSONResponse(status_code=400, content={"error": "Sensitive information found"})
        response = await call_next(request)
        return response