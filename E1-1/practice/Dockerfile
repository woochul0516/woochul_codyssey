FROM nginx:alpine
LABEL maintainer="student"
LABEL description="Custom Nginx Web Server for Dev Workstation"
COPY app/index.html /usr/share/nginx/html/index.html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
