const fs = require('fs');
const path = require('path');

describe('index.html basic checks', () => {
  let html;
  beforeAll(() => {
    html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
  });

  test('creates alertsPane for overlays above radar', () => {
    expect(html).toMatch(/map\.createPane\(['"]alertsPane['"]\)/);
    expect(html).toMatch(/getPane\(['"]alertsPane['"]\)\.style\.zIndex\s*=\s*700/);
  });

  test('ALERT_PLAIN includes Warning mapping', () => {
    expect(html).toMatch(/const\s+ALERT_PLAIN\s*=\s*\{[\s\S]*?['"]Warning['"]\s*:/);
  });

  test('updateBanner DOM element exists', () => {
    expect(html).toMatch(/id=["']updateBanner["']/);
    expect(html).toMatch(/id=["']editUpdate["']/);
    expect(html).toMatch(/id=["']announceUpdateBtn["']/);
  });
});
