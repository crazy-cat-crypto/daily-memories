export default {
  async email(message, env, ctx) {
    const rawResponse = new Response(message.raw);
    const fullBody = await rawResponse.text();

    const parts = fullBody.split(/\r?\n\r?\n/);
    let cleanBody = parts.slice(1).join("\n\n");


    const boundaryMatch = fullBody.match(/boundary="?([^"\r\n;]+)"?/i);
    if (boundaryMatch) {
      const boundary = boundaryMatch[1];
      const sections = cleanBody.split("--" + boundary);
      for (const section of sections) {
        if (section.includes("text/plain")) {
          cleanBody = section.split(/\r?\n\r?\n/).slice(1).join("\n\n").trim();
          break;
        }
      }
    }

    await fetch("https://daily-memories.baral-aayush.com.np/cache-email", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        from: message.from,
        subject: message.headers.get("subject") || "No Title",
        body: cleanBody.trim() || "Empty Body"
      })
    });
  }
}