/* =========================================================
   Client carousel data  -  edit / add your real clients here.
   Fields (all optional except name):
     name   : client name (shown if no logo image)
     logo   : path to a logo image, e.g. "assets/clients/acme-logo.png"
     image  : path to the card background photo
     stat   : big number, e.g. "+133%"
     label  : small text under the number
     bare   : true if the image already has the logo/name on it (hides the text name,
              keeps the stat at the bottom)
     bg     : fallback CSS background if no image
   ========================================================= */
window.GWADAR_CLIENTS = [
  { name: "Client One",   stat: "+100%", label: "Website Engagement",        image: "", logo: "", bg: "linear-gradient(160deg,#1b8fd9,#0b1654)" },
  { name: "Junk Patrol", stat: "+179%", label: "Organic Traffic Value", image: "assets/clients/junk-patrol.webp", logo: "", bare: true, bg: "linear-gradient(160deg,#8b5cf6,#1a0f4d)" },
  { name: "Victor Super Premium Pet Food", stat: "134%",  label: "Increase in engagement rate", image: "assets/clients/victor.webp", logo: "", bare: true, bg: "linear-gradient(160deg,#ff6a13,#5a1d00)" },
  { name: "Joaquin Painting", stat: "290%",  label: "Increase in conversions", image: "assets/clients/joaquin-painting.webp", logo: "", bare: true, bg: "linear-gradient(160deg,#16c04b,#06351a)" },
  { name: "Tyris Tile and Renovations", stat: "172%",  label: "Increase in organic website traffic", image: "assets/clients/tyris-tile-renovations.webp", logo: "", bare: true, bg: "linear-gradient(160deg,#2de1d6,#073a46)" },
  { name: "Sharkey's Cuts for Kids", stat: "4.8x",  label: "Return on ad spend", image: "assets/clients/sharkeys-cuts-for-kids.webp", logo: "", bare: true, bg: "linear-gradient(160deg,#e0457b,#3d0a24)" }
];
