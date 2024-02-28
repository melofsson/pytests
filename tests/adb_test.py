import subprocess

def test_adb_list_devices_C156127():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    assert "192.168.10.198:5555" in result.stdout
   


