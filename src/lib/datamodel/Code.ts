export class Code {
  public documentID: Number;
  public themeID: Number;
  public content: String;
  public startPos: Number;
  public endPos: Number;
  public length: Number;

  public constructor(documentID: Number, themeID: Number, content: String, startPos: Number, endPos: Number, length: Number) {
    this.documentID = documentID;
    this.themeID = themeID;
    this.content = content;
    this.startPos = startPos;
    this.endPos = endPos;
    this.length = length;
  }
}