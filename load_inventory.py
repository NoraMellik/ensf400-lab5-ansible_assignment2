import ansible_runner

def ping():
    results = ansible_runner.run(
        private_data_dir='.', 
        playbook='ping.yml'
    )
    
    if results.status == "successful":
        print("Ping successful.")
    else:
        print("Ping failed.")

    for host, stats in results.stats.items():
        print(f"Host: {host}, Stats: {stats}")

if __name__ == "__main__":
    ping()
