export class Doc {
  public id: Number;
  public title: String;
  public content: String;
  public attributes: Map<String, any>;

  public constructor(id: Number, title: String, content: String, attributes: Map<String, any>) {
    this.id = id;
    this.title = title;
    this.content = content;
    this.attributes = attributes;
  }

  public toJSON(): any {
    return {
      __type: "Doc",  // identify the class type
      id: this.id,
      title: this.title,
      content: this.content,
      // Convert each subclass to JSON using its own toJSON()
      attributes: Array.from(this.attributes.entries()).map(([key, value]) => ({ key, value }))
    };
  }
  
  public static fromJSON(json: any) {
    return new Doc(
      json.id, 
      json.title, 
      json.content,
      json.attributes ? new Map(json.attributes.map((attr: any) => [attr.key, attr.value])) : new Map<String, any>()
    );
  }
}