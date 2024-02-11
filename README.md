# Qualitative and Quantitative analysis of PostgreSQL connection poolers

This repo contains information to reproduce the results presented in Tembo's blog post.

Here you'll find:

- Configuration files
- Jupyter notebooks

As a reminder, I used a VM with the following characteristics:

| | |
|----------------------|-----------------------------------------------|
| **VM**               | E2-standard-8 (8 vCPUs, 4 cores, 32GB memory) |
| **Storage**          | 100GB                                         |
| **Operating System** | Debian 11.8                                   |
| **Postgres**         | 15.5                                          |
| **Pgbouncer**        | v1.21                                         |
| **Pgcat**            | v1.1.1                                        |
| **Supavisor**        | v1.1.13                                       |
