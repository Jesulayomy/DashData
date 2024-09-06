import axios from "axios";

const api = axios.create({
  baseURL: "https://blockhouse-api.jesulayomi.tech/api/",
});

export { api };
