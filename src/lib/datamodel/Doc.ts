export class Doc {
  public id: Number;
  public title: String;
  public content: String;

  public constructor(id: Number, title: String, content: String ) {
    this.id = id;
    this.title = title;
    this.content = content;
  }

  public toJSON(): any {
    return {
      __type: "Doc",  // identify the class type
      id: this.id,
      title: this.title,
      content: this.content,
    };
  }
  
  public static fromJSON(json: any) {
    return new Doc(
      json.id, 
      json.title, 
      json.content
    );
  }
}