# Cloud Resource Orchestration System with Auto Scaling

A Cloud-Based Resource Orchestration System with Auto Scaling capabilities that demonstrates automated resource management based on simulated CPU metrics.

## Overview

This project implements a simple yet effective cloud resource orchestration controller that automatically scales computing resources up or down based on CPU usage metrics. The system is designed to maintain optimal resource utilization while ensuring application performance.

## Features

- **Auto Scaling**: Automatically scales resources based on CPU usage thresholds
- **Configurable Thresholds**: Customizable high and low CPU thresholds for scaling decisions
- **Instance Management**: Maintains minimum and maximum instance counts
- **Real-time Monitoring**: Simulated CPU metrics monitoring and logging
- **Decision Logging**: Detailed logging of all scaling decisions with timestamps

## Project Structure

```
cloud-resource-orchestration/
├── src/
│   └── main.py           # Main orchestration controller
├── docs/
│   └── architecture.md   # System architecture documentation
├── configs/
│   └── config.yaml       # Configuration file for orchestration parameters
└── README.md             # This file
```

## How It Works

The orchestration controller follows this workflow:

1. **Monitor**: Continuously monitors CPU usage metrics
2. **Evaluate**: Compares current CPU usage against configured thresholds
3. **Scale**: Makes scaling decisions based on evaluation:
   - Scale up if CPU usage exceeds high threshold
   - Scale down if CPU usage falls below low threshold
   - Maintain current state if within acceptable range
4. **Log**: Records all actions with timestamps for audit and analysis

## Usage

### Running the Orchestrator

```bash
python src/main.py
```

### Configuration

The orchestrator can be configured with the following parameters:

- `min_instances`: Minimum number of instances to maintain (default: 2)
- `max_instances`: Maximum number of instances allowed (default: 8)
- `cpu_threshold_high`: CPU percentage to trigger scale-up (default: 70%)
- `cpu_threshold_low`: CPU percentage to trigger scale-down (default: 35%)

## Example Output

```
======================================================================
Cloud Resource Orchestration System - Auto Scaling Demo
======================================================================
Configuration:
  Min Instances: 2
  Max Instances: 8
  CPU High Threshold: 70%
  CPU Low Threshold: 35%
======================================================================

--- Iteration 1/15 ---
[2025-10-26 14:20:30] Current CPU: 45.23% | Instances: 2
CPU usage within acceptable range. No scaling needed.

--- Iteration 2/15 ---
[2025-10-26 14:20:31] Current CPU: 78.56% | Instances: 2
CPU usage (78.56%) exceeds high threshold (70%)
[2025-10-26 14:20:31] SCALE UP: Added instance. Total instances: 3
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Future Enhancements

- Integration with actual cloud providers (AWS, Azure, GCP)
- Support for multiple metrics (memory, network, disk I/O)
- Advanced scaling algorithms (predictive scaling, ML-based)
- RESTful API for remote management
- Web dashboard for monitoring and control
- Support for containerized workloads (Kubernetes integration)

## License

This is a demonstration project for educational purposes.

## Author

Developed as a mini-project for cloud resource orchestration studies.
