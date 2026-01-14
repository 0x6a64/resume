/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {},
	},
	plugins: [require("@tailwindcss/typography"),require("daisyui")],
	daisyui: {
		themes: [
			{
				kanagawa: {
					"primary": "#7E9CD8",          // base0D - Blue
					"primary-content": "#1F1F28", // base00 - Dark background
					"secondary": "#957FB8",       // base0E - Purple
					"secondary-content": "#1F1F28",
					"accent": "#C0A36E",          // base0A - Yellow/gold
					"accent-content": "#1F1F28",
					"neutral": "#54546D",         // base03 - Muted
					"neutral-content": "#DCD7BA", // base05 - Main text
					"base-100": "#1F1F28",        // base00 - Background
					"base-200": "#16161D",        // base01 - Darker background
					"base-300": "#223249",        // base02 - Selection/highlights
					"base-content": "#DCD7BA",    // base05 - Main text
					"info": "#6A9589",            // base0C - Cyan/teal
					"info-content": "#1F1F28",
					"success": "#76946A",         // base0B - Green
					"success-content": "#1F1F28",
					"warning": "#FFA066",         // base09 - Orange
					"warning-content": "#1F1F28",
					"error": "#C34043",           // base08 - Red
					"error-content": "#DCD7BA",
				},
			},
		],
		darkTheme: "kanagawa",
		logs: false,
	}
}
