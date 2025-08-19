new updates coming soon:) plan to add hurricane tracks

# Weather Alerts Revamp

A web app that displays live weather alerts from the US National Weather Service (NWS), overlays them on a map, and lets you toggle the latest NWS radar mosaic.  
Built with HTML, Bootstrap, and Leaflet – no backend required.

## Features

- **Live NWS Alerts:** Fetches all current US NWS alerts from [weather.gov](https://www.weather.gov/).
- **Map Visualization:** Alerts are shown on an interactive map using [Leaflet](https://leafletjs.com/), with polygons/areas and points correctly colored by severity.
- **NWS Radar Overlay:** Toggle the latest NWS radar mosaic (reflectivity) as a semi-transparent overlay above the base map and below the warnings.
- **Responsive Design:** Works on desktop and mobile.
- **Dark Mode:** Toggle dark mode for better nighttime viewing.
- **Filters & Search:** Search alerts by text or filter by severity.
- **Location Filter:** Show only alerts near your current location (uses browser geolocation).
- **No Backend Needed:** Fully static, just serve the HTML file.

## How to Use

1. **Open `index.html`** in any modern browser.  
   You can host it anywhere (GitHub Pages, Netlify, Vercel, S3, etc.)

2. **Map Controls:**
   - Use the "Show Alerts For My Location" button to center and filter to your location.
   - Search and filter alerts using the input and dropdown.
   - Use the "Toggle Radar" button to turn the radar overlay on or off.
   - Toggle dark mode with the 🌙 button in the top bar.

3. **Viewing Alerts:**
   - Alerts appear as colored polygons or markers.
   - Click any polygon or marker for details and a link to the official alert.

## Technical Details

- **Alerts:** Fetched live from [`https://api.weather.gov/alerts/active`](https://api.weather.gov/alerts/active)
- **Radar:** WMS overlay from [NOAA OpenGeo](https://opengeo.ncep.noaa.gov/geoserver/web/)
- **Map:** [OpenStreetMap](https://www.openstreetmap.org/) tiles via Leaflet
- **No API Key Required**

### Alert Polygon Coloring

- **Red**: Warning
- **Orange/Yellow**: Watch
- **Blue**: Advisory

### Radar Layer

- Source: [NOAA/NWS NEXRAD Composite](https://opengeo.ncep.noaa.gov/geoserver/conus/conus_bref_qcd/ows)
- Opacity is set to 0.6 by default (adjust in code if desired).
- Always appears *under* the alert polygons/markers.

## Accessibility & Browser Support

- Uses semantic HTML and ARIA labels for accessibility.
- Geolocation may require HTTPS.
- Works in all modern browsers (Chrome, Firefox, Edge, Safari).

## Attribution

- Weather alerts and radar by [NOAA/NWS](https://www.weather.gov/).
- Map data by [OpenStreetMap](https://www.openstreetmap.org/).
- Built with [Leaflet](https://leafletjs.com/) and [Bootstrap](https://getbootstrap.com/).

## License

MIT License.

---

*This is a static, client-only project. No personal data is collected or stored.*
