module.exports = {
  content: ["./pages/cours/index.vue"],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#8B4A24",
          dark: "#693619",
        },
        secondary: {
          DEFAULT: "#D89B2B",
          light: "#F0B94E",
        },
        background: "#FAF5EA",
        surface: {
          DEFAULT: "#FFFDF7",
          muted: "#F1E2C8",
        },
        foreground: {
          DEFAULT: "#3B271A",
          dark: "#2F1D14",
          muted: "#5A3A25",
          subtle: "#76543A",
          faint: "#9A806B",
        },
        outline: {
          DEFAULT: "#D6B98C",
          subtle: "#E5D3B5",
        },
      },
    },
  },
  safelist: [
    {
      pattern: /^bg-.+$/,
    },
    {
      pattern: /^text-.+$/,
    },
  ],
};
