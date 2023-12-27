/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: [
      "unsplash.it",
      "images.unsplash.com",
      "picsum.photos",
      "i.dummyjson.com",
    ],
  },
};

module.exports = nextConfig;
