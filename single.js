import http from 'k6/http';


export let options = {
    vus: 80,
    duration: '30s',
    ext: {
      loadimpact: {
        projectID: 3542013,
        name: "asgi_benchmark"
      }
    }
}

export function setup() {
}

const http_server_url = 'http://localhost:8000';

export default function (data) {
  const url = `${http_server_url}/`;
  const res =  http.get(url)
}

export function teardown(data) {
}
