import os
import subprocess

def mkdir_and_chown(path, owner=None):
    if owner is None:
        # Get current user and group from id command
        result = subprocess.run(['id'], capture_output=True, text=True)
        id_output = result.stdout.strip()
        
        # Extract username from uid=584138329(username) part
        import re
        user_match = re.search(r'uid=\d+\(([^)]+)\)', id_output)
        group_match = re.search(r'gid=\d+\(([^)]+)\)', id_output)
        
        username = user_match.group(1) if user_match else 'root'
        groupname = group_match.group(1) if group_match else 'root'
        owner = f"{username}:{groupname}"
    
    os.system("mkdir -p " + path)
    os.system(f"chown '{owner}' " + path)

os.system("whoami")
os.system("ls -l /mnt")

# Mount blob1
# Do not use "/mnt/output" as mount point
mkdir_and_chown("/mnt/pretrain")
mkdir_and_chown("/mnt/cache/pretrain")
# os.system("blobfuse2 unmount /mnt/pretrain")
os.system("blobfuse2 mount /mnt/pretrain --config-file=hanzhang_config.yaml")

# If needed mount blob2
# ......

os.system("ls -l /mnt/pretrain")