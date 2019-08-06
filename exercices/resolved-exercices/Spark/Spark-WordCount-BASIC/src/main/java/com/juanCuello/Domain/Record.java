package com.juanCuello.Domain;

public class Record {

   String ip;
   String time;
   String url;
   String status;

    public Record(String ip, String time, String url, String status) {
        this.ip = ip;
        this.time = time;
        this.url = url;
        this.status = status;
    }

    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
