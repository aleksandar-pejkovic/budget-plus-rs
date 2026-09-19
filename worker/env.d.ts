// Secrets are configured in the Cloudflare secret store, never in public site assets.
interface Env {
  TURNSTILE_SECRET: string;
  SMTP_PASSWORD: string;
}
