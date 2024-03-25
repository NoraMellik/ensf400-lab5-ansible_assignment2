import ansible_runner

def run_hello_playbook():
    results = ansible_runner.run(
        private_data_dir='.', 
        playbook='hello.yml'
    )
    
    print("Playbook executed with status:", results.status)
    for host, stats in results.stats.items():
        print(f"Host: {host}, Stats: {stats}")

if __name__ == "__main__":
    run_hello_playbook()