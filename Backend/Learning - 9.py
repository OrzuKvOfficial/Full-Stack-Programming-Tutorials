from jnius import autoclass

# Access Android context and connectivity services
Context = autoclass('android.content.Context')
ConnectivityManager = autoclass('android.net.ConnectivityManager')

# Function to check Wi-Fi status
def is_wifi_enabled():
    # Get the Connectivity Manager
    context = autoclass('org.kivy.android.PythonActivity').mActivity
    connectivity_manager = context.getSystemService(Context.CONNECTIVITY_SERVICE)
    
    # Get network info
    network_info = connectivity_manager.getActiveNetworkInfo()
    
    # Check if the device is connected to Wi-Fi
    if network_info is not None and network_info.getType() == ConnectivityManager.TYPE_WIFI:
        return network_info.isConnected()
    return False

print("Wi-Fi Enabled:", is_wifi_enabled())
