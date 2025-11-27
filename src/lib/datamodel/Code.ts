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

  public toJSON(): any {
    return {
      __type: "Code",  // identify the class type
      documentID: this.documentID,
      themeID: this.themeID,
      content: this.content,
      startPos: this.startPos,
      endPos: this.endPos,
      length: this.length
    };
  }

  public static fromJSON(json: any) {
    return new Code(
      json.documentID, 
      json.themeID,
      json.content,
      json.startPos,
      json.endPos,
      json.length
    );
  }
}