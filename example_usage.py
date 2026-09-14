import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import MultiTenantAgentIsolationSandboxClient

def main():
    client = MultiTenantAgentIsolationSandboxClient()
    res = client.enforce_tenant_isolation()
    print("=== Multi-Tenant Agent Isolation Sandbox Output ===")
    print(f"Status: {res['sandbox_status']} | Tenant: {res['tenant_id']}")
    print(f"Scope Token: {res['tenant_scope_token']}")
    print(f"Cross-Tenant Leak Detected: {res['cross_tenant_leak_detected']}")
    print(f"Isolated Memory Ready: {res['isolated_memory_frame_ready']}")

if __name__ == '__main__':
    main()
