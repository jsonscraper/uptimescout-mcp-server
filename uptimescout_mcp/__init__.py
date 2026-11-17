import urllib.request
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None
_open=urllib.request.build_opener(NoRedirect()).open
"""stdio ↔ Streamable HTTP bridge. Secrets are never printed."""
import os,sys,json,urllib.request,urllib.error

def main():
 key=os.environ.get("UPTIMESCOUT_LICENSE_KEY","")
 if not key:sys.stderr.write("Set UPTIMESCOUT_LICENSE_KEY from Evelode.com.\n");return 1
 for line in sys.stdin:
  try:
   message=json.loads(line);req=urllib.request.Request("https://mcp.uptimescout.com/mcp",data=json.dumps(message).encode(),headers={"Authorization":"Bearer "+key,"Content-Type":"application/json","Accept":"application/json, text/event-stream"})
   with _open(req,timeout=35) as response:
    raw=response.read(4*1024*1024)
   if raw:sys.stdout.write(json.dumps(json.loads(raw))+"\n");sys.stdout.flush()
  except Exception:
   if isinstance(locals().get("message"),dict) and "id" in message:sys.stdout.write(json.dumps({"jsonrpc":"2.0","id":message["id"],"error":{"code":-32603,"message":"UptimeScout request failed. Check your connection and license."}})+"\n");sys.stdout.flush()
 return 0
