export class Doc {
  public id: Number;
  public title: String;
  public content: String;

  public constructor(id: Number, title: String, content: String ) {
    this.id = id;
    this.title = title;
    this.content = content;
  }
}