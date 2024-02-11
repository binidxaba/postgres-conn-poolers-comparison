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


## OS Configuration

The following changes were made to avoid socket reuse problems:

```bash
echo 1 > /proc/sys/net/ipv4/tcp_tw_reuse
echo "1025 65535" > /proc/sys/net/ipv4/ip_local_port_range
```

The following change was made to avoid reaching `fd` limit:

```bash
ulimit -n 10000
```

