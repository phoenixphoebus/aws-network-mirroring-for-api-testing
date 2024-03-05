# aws-network-mirroring-for-api-testing

## Why does this repo exist?
This repo contains steps and code to use AWS traffic mirroring for REST API testing. The most common use case would be to mirror Production traffic and test if changes to an API break over production traffic. Others can be for Security, traffic analysis, etc.

## What is AWS Network mirroring?
The official answer is here - https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html

TLDR - Its a feature that allows replaying packets that cross an ENI (both ways) to another ENI. The key here is - *ENI*. The replay is over UDP so the disadvantages of UDP apply.

## How will we demonstrate API testing?
* Creation of a REST API is beyond the scope of this guide but two nginx servers that return a JSON would be used for the demo.
* It is also assumed that you are familiar with AWS network and cases such as mirroring traffic across accounts or VPCs is beyond the scope of this guide. For mirroring traffic across accounts, one can use AWS RAM (Resource Access Manager) and for across VPCs one could use VPC sharing/peering. This guide would run two ec2 machines running in the same private subnet, one of which accepts requests on port 80 from the internet.
* This guide would use an open source library - Scapy to listen for incoming packets, and match request packets with response packets.

## Steps
