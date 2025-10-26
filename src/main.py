#!/usr/bin/env python3
"""
Cloud-Based Resource Orchestration System with Auto Scaling
Simple orchestration controller that scales resources based on simulated CPU metrics
"""

import time
import random
from datetime import datetime


class ResourceOrchestrator:
    """Main orchestration controller for managing cloud resources"""
    
    def __init__(self, min_instances=1, max_instances=10, cpu_threshold_high=75, cpu_threshold_low=30):
        self.min_instances = min_instances
        self.max_instances = max_instances
        self.cpu_threshold_high = cpu_threshold_high
        self.cpu_threshold_low = cpu_threshold_low
        self.current_instances = min_instances
        
    def get_simulated_cpu_usage(self):
        """Simulate CPU usage metrics (0-100%)"""
        return random.uniform(20, 95)
    
    def scale_up(self):
        """Scale up resources by adding an instance"""
        if self.current_instances < self.max_instances:
            self.current_instances += 1
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SCALE UP: Added instance. Total instances: {self.current_instances}")
            return True
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Max instances reached. Cannot scale up.")
            return False
    
    def scale_down(self):
        """Scale down resources by removing an instance"""
        if self.current_instances > self.min_instances:
            self.current_instances -= 1
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SCALE DOWN: Removed instance. Total instances: {self.current_instances}")
            return True
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Min instances reached. Cannot scale down.")
            return False
    
    def evaluate_and_scale(self, cpu_usage):
        """Evaluate current metrics and make scaling decisions"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Current CPU: {cpu_usage:.2f}% | Instances: {self.current_instances}")
        
        if cpu_usage > self.cpu_threshold_high:
            print(f"CPU usage ({cpu_usage:.2f}%) exceeds high threshold ({self.cpu_threshold_high}%)")
            self.scale_up()
        elif cpu_usage < self.cpu_threshold_low:
            print(f"CPU usage ({cpu_usage:.2f}%) below low threshold ({self.cpu_threshold_low}%)")
            self.scale_down()
        else:
            print("CPU usage within acceptable range. No scaling needed.")
    
    def run(self, iterations=10, delay=2):
        """Run the orchestration loop"""
        print("="*70)
        print("Cloud Resource Orchestration System - Auto Scaling Demo")
        print("="*70)
        print(f"Configuration:")
        print(f"  Min Instances: {self.min_instances}")
        print(f"  Max Instances: {self.max_instances}")
        print(f"  CPU High Threshold: {self.cpu_threshold_high}%")
        print(f"  CPU Low Threshold: {self.cpu_threshold_low}%")
        print("="*70)
        print()
        
        for i in range(iterations):
            print(f"\n--- Iteration {i+1}/{iterations} ---")
            cpu_usage = self.get_simulated_cpu_usage()
            self.evaluate_and_scale(cpu_usage)
            time.sleep(delay)
        
        print("\n" + "="*70)
        print(f"Orchestration cycle completed. Final instances: {self.current_instances}")
        print("="*70)


if __name__ == "__main__":
    # Initialize the orchestrator with default settings
    orchestrator = ResourceOrchestrator(
        min_instances=2,
        max_instances=8,
        cpu_threshold_high=70,
        cpu_threshold_low=35
    )
    
    # Run the orchestration loop
    orchestrator.run(iterations=15, delay=1)
