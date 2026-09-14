import json, sys
from client import MultiTenantAgentIsolationSandboxClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "multi-tenant-isolation", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "enforce_tenant_isolation", "description": "Enforces cryptographic multi-tenant sandbox boundaries for enterprise agents."}]}}
    elif method == "tools/call":
        client = MultiTenantAgentIsolationSandboxClient()
        res = client.enforce_tenant_isolation()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = MultiTenantAgentIsolationSandboxClient()
        print(json.dumps(client.enforce_tenant_isolation(), indent=2))
