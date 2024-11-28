# Wirefox

**Wirefox** is a compact, headless device based on the Luckfox Pico Plus/Pro/Max, designed for SecOps professionals and pentesters. It simplifies setting up a proxy by automatically configuring itself when connected to power and Ethernet.  

**Wirefox Services** is the backbone of this system, enabling users to retrieve the device's local and public IPs effortlessly without network scanning. This makes managing headless devices seamless and efficient.

---

## Features

- **Automatic IP Discovery**: Detects and uploads local and public IPv4 addresses to a GitHub Gist.
- **Duplicate Prevention**: Ensures only new IP addresses are uploaded.
- **Timestamps**: Includes a log of when each IP was recorded.
- **Configurable**: Easily customize behavior with a `wirefox.conf` file.
- **System Service**: Runs at boot for plug-and-play usability.

---

## About Wirefox

Wirefox is an all-in-one solution for simplifying remote proxy setup. With its lightweight design and powerful Python backend, Wirefox is the ideal tool for SecOps and pentesting professionals needing a quick and reliable SOCKS5 proxy.

Whether you're using it for remote operations or as part of a broader infrastructure, Wirefox delivers ease of use, reliability, and precision.
