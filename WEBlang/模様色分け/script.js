let s; // for Snap
let width;
let height;

const sqrt3 = Math.sqrt(3);
const lw = 50; // leaf width
const lh = 25 * sqrt3; // leaf height

/**
 * drawLeaf function
 * @since 0.2
 */
const drawLeaf = function (x, y, fillColor) {
  // 外枠を描画
  s.line(x, y, x + lw, y).attr({ stroke: "black", strokeWidth: lw * 0.04 });
  s.line(x + lw / 2, y, x + lw / 2, y + (sqrt3 - 0.5) / sqrt3 * lh).attr({
    stroke: "black",
    strokeWidth: lw * 0.04,
  });
  s.line(x, y + 0.5 / sqrt3 * lh, x, y + lh).attr({
    stroke: "black",
    strokeWidth: lw * 0.04,
  });
  s.line(x + lw / 2, y, x, y + lh).attr({
    stroke: "black",
    strokeWidth: lw * 0.04,
  });
  s.line(x + lw / 2, y, x + lw, y + lh).attr({
    stroke: "black",
    strokeWidth: lw * 0.04,
  });
  s.line(x + lw / 2, y, x, y + 0.5 / sqrt3 * lh).attr({
    stroke: "black",
    strokeWidth: lw * 0.04,
  });
  s.line(x + lw / 2, y, x + lw, y + 0.5 / sqrt3 * lh).attr({
    stroke: "black",
    strokeWidth: lw * 0.04,
  });
  s.line(x + lw / 2, y + (sqrt3 - 0.5) / sqrt3 * lh, x, y + lh).attr({
    stroke: "black",
    strokeWidth: lw * 0.04,
  });
  s.line(x + lw / 2, y + (sqrt3 - 0.5) / sqrt3 * lh, x + lw, y + lh).attr({
    stroke: "black",
    strokeWidth: lw * 0.04,
  });

  // エリアを塗る
  s.polygon([x, y, x + lw / 2, y + lh, x, y + lh]).attr({
    fill: fillColor,
  });
};

/**
 * onload function
 * @since 0.2
 */
window.onload = function () {
  // Get svg element
  s = Snap("#Pattern");
  width = s.getBBox().width;
  height = s.getBBox().height;

  // 初期色
  let fillColor = document.getElementById("fillColor").value;

  // カラーパレットの変更に応じて再描画
  document.getElementById("fillColor").addEventListener("input", function () {
    fillColor = this.value;
    drawPattern(fillColor);
  });

  drawPattern(fillColor);
};

// パターンを描画する関数
function drawPattern(fillColor) {
  s.clear(); // SVGをクリア
  let x0 = 0;
  for (let y = 0; y <= height; y += lh) {
    for (let x = x0; x <= width; x += lw) {
      drawLeaf(x, y, fillColor);
    }
    if (x0 === 0) {
      x0 = -lw / 2;
    } else {
      x0 = 0;
    }
  }
}
