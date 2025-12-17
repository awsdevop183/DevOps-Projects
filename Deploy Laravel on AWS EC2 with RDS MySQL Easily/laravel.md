# 🚀 Deploy Laravel on AWS EC2 with RDS MySQL  
### Complete DevOps Setup (Nginx + PHP 8.2 + SSL)

This guide walks through deploying a **Laravel application on AWS EC2**, connecting it to **AWS RDS MySQL**, configuring **Nginx**, **PHP-FPM**, and securing the application with **HTTPS using Certbot**.

---

## 🧰 Prerequisites

- AWS EC2 (Ubuntu 22.04 recommended)
- AWS RDS MySQL instance
- Domain name pointing to EC2 public IP
- SSH access to EC2 instance

---

## 🔄 System Update

```bash
sudo apt update && sudo apt upgrade -y

sudo apt install -y curl git unzip software-properties-common

sudo apt install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx

sudo add-apt-repository ppa:ondrej/php -y
sudo apt update

sudo apt install -y php8.2-fpm php8.2-cli php8.2-common php8.2-mysql \
php8.2-xml php8.2-curl php8.2-gd php8.2-mbstring php8.2-zip \
php8.2-bcmath php8.2-intl php8.2-readline php8.2-tokenizer

php -v
sudo systemctl status php8.2-fpm

cd ~
curl -sS https://getcomposer.org/installer -o composer-setup.php
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
rm composer-setup.php

composer --version

sudo apt install -y mysql-client

cd /var/www
sudo composer create-project laravel/laravel laravel-app

sudo chown -R www-data:www-data /var/www/laravel-app
sudo chown -R $USER:www-data /var/www/laravel-app

sudo chmod -R 775 /var/www/laravel-app/storage
sudo chmod -R 775 /var/www/laravel-app/bootstrap/cache

cd /var/www/laravel-app
sudo vi .env

php artisan key:generate
php artisan config:clear
php artisan config:cache

php artisan migrate

sudo vi /etc/nginx/sites-available/awshero.shop

 ```
 server {
    listen 80;
    listen [::]:80;

    server_name awshero.shop www.awshero.shop;
    root /var/www/laravel-app/public;

    index index.php index.html index.htm;

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    access_log /var/log/nginx/laravel_access.log;
    error_log /var/log/nginx/laravel_error.log;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
        fastcgi_hide_header X-Powered-By;
    }

    location ~ /\.(?!well-known).* {
        deny all;
    }

    location ~* \.(jpg|jpeg|png|gif|ico|css|js|pdf|txt)$ {
        expires 7d;
        add_header Cache-Control "public, immutable";
    }
}

  ```

sudo ln -s /etc/nginx/sites-available/awshero.shop /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
sudo apt install -y certbot python3-certbot-nginx
sudo apt install -y certbot python3-certbot-nginx
sudo certbot renew --dry-run
sudo systemctl status certbot.timer

✅ Final Result

Laravel running on AWS EC2
Connected securely to RDS MySQL
Nginx + PHP-FPM configured
HTTPS enabled with auto-renewal
Production-ready DevOps setup 🚀

📌 Author

Madhukar Reddy
AWS & DevOps | Real-World Projects
YouTube: https://youtube.com/@awsandevops


---

If you want, I can also:
- Optimize this README for **GitHub stars**
- Add **architecture diagram (ASCII or image)**
- Convert this into a **blog post or Medium article**
- Create **CI/CD section (GitHub Actions)**

Just say the word 💪