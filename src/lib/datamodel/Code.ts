export class Code {
  public documentID: Number;
  public themeID: Number;
  public content: String;

  public constructor(documentID: Number, themeID: Number, content: String ) {
    this.documentID = documentID;
    this.themeID = themeID;
    this.content = content;
  }
}