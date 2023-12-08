# portProbe - Full Port Scanner

- portProbe is a Python-based tool designed for efficient probing of open ports on a target system.
  
- The tool supports both TCP and UDP port scanning on specified IP addresses or domains.

- It utilizes multithreading for faster scanning and allows users to save results to an output file.
  
-  Works in all platforms.

## Installation

- Clone the repository to your local machine.
  
- Install the required dependencies using pip


```bash
git clone https://github.com/aashish36/portProbe.git

cd portProbe

pip install -r requirements.txt

```

## Usage

- Create a file containing that contains list of Ip Address or subdomains or both and give to portProbe.

- This python code will save the results of the analysis to a file named 'output.txt'.

- Run the script using the following commands: 

``` bash

portProbe is a tool designed to efficiently probe for open ports. It will take both IP Address and Subdomains.

options:
  -h, --help            show this help message and exit

  -d Domain, --Domain Domain
                        [INFO]: Domain to probe.

  -dL DomainList, --DomainList DomainList
                        [INFO]: List of Domain to probe.

  -i ip, --ip ip        [INFO]: IP Address to probe.

  -iL IpList, --IpList IpList
                        [INFO]: List of Ip to probe.

  -o output, --output output
                        [INFO]: File to save our output.

```
## Tool Output

![image](https://github.com/aashishsec/portProbe/assets/65489287/8afa9812-d608-4f28-b93b-07b2b920eb44)


## Contributing

- Contributions are welcome!
  
- If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

![image](https://github.com/aashish36/JSScanner/assets/65489287/70f7e3a8-e95f-429b-9433-89087daad721)

