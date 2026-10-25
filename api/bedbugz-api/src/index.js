/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run `npm run dev` in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */
import PROFILES from "./new_profiles.json";

const PER_PAGE = 5
const CORS_HEADERS = {
	"Access-Control-Allow-Origin": "https://bedbugz.thejmc.co.uk",
	"Access-Control-Allow-Methods": "GET,POST,PUT,PATCH,DELETE,OPTIONS",
	"Access-Control-Allow-Headers": "Content-Type, Authorization",
};

function withCors(response) {
	const headers = new Headers(response.headers);
	for (const [key, value] of Object.entries(CORS_HEADERS)) {
		headers.set(key, value);
	}

	return new Response(response.body, {
		status: response.status,
		statusText: response.statusText,
		headers,
	});
}


// Returns the first complete {...} object in text, ignoring anything around it
function firstJsonObject(text) {
	const start = text.indexOf("{");
	if (start === -1) return text;
	let depth = 0;
	let inString = false;
	for (let i = start; i < text.length; i++) {
		const ch = text[i];
		if (inString) {
			if (ch === "\\") i++;
			else if (ch === '"') inString = false;
		} else if (ch === '"') {
			inString = true;
		} else if (ch === "{") {
			depth++;
		} else if (ch === "}" && --depth === 0) {
			return text.slice(start, i + 1);
		}
	}
	return text.slice(start);
}

export default {
	async fetch(request, env, ctx) {
		if (request.method === "OPTIONS") {
			return new Response(null, { status: 204, headers: CORS_HEADERS });
		}

		const url = new URL(request.url);

		if (url.pathname.startsWith("/chat/")) {
			const bugName = url.pathname.split("/")[2];
			const model = env.AI_MODEL || "@cf/meta/llama-3.1-8b-instruct";
			const prompt = "Please generate 2 of the below response. You are pretending to be an insect bug on tinder. You are a [bug]. You are sexy and educational. Do not give an introduction.Please can you generate a message \
        from you, the bug, to another bug. Can you try to keep the responses concise please. Please respond exactly in the format, with no extra text at the beginning, or markers for code blocks - you are sending this directly to a JSON parser \
        Please respond in JSON format, with a string field 'bugMsg', then a dict called 'responses' which contains 'good', 'medium', 'bad'.".replace("[bug]", bugName);

			let text;
			if (model.startsWith("@cf/")) {
				// Cloudflare-hosted Workers AI model
				const response = await env.bedbugz_ai.run(model, { prompt, max_tokens: 512 });
				text = response.response;
			} else {
				// Third-party model (e.g. anthropic/claude-haiku-5.5) via AI Gateway
				const response = await env.bedbugz_ai.run(
					model,
					{ max_tokens: 1024, messages: [{ role: "user", content: prompt }] },
					{ gateway: { id: "default" } },
				);
				text = response.content.find((block) => block.type === "text").text;
			}
			console.log(model, text)
			// models sometimes add fences or extra objects, so only parse the first one
			let result = JSON.parse(firstJsonObject(text));
			return withCors(new Response(JSON.stringify(result)));
		}

		if (url.pathname.startsWith("/profile/")) {
			const pageNum = url.pathname.split("/")[2];
			let length = PROFILES.length;
			length = PROFILES.length;
			let num_pages = Math.ceil(length / PER_PAGE);
			if (pageNum > num_pages) {
				return withCors(new Response(JSON.stringify({error: "Page number out of range"}), {status: 400}));
			}
			let start = (pageNum - 1) * PER_PAGE;
			let end = start + PER_PAGE;
			// shuffle the profiles so that we get a different set each time
			PROFILES.sort(() => Math.random() - 0.5);

			let result = {"num_of_pages": num_pages, "current_page": pageNum, "profiles": PROFILES.slice(start, end)};
			return withCors(new Response(JSON.stringify(result)));
		}

		return withCors(new Response("Hello World!"));
	},
};
