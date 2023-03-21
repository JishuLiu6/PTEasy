  /**
   * 获取本地图
   * @param name // 文件名 如 doc.png
   * @returns {*|string}
   */
  export function imgUrl(name) {
    console.log(`@/assets/images/${name}`)
    return new URL(`../assets/images/${name}`, import.meta.url).href;
  }

 