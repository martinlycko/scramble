export class Theme {
  public id: Number;
  public title: String;

  public constructor(id: Number, title: String ) {
    this.id = id;
    this.title = title;
  }

  public toJSON() {
    return {
      __type: "Theme",  // identify the class type
      id: this.id,
      title: this.title,
    };
  }

  public fromJSON(json: any) {
    return new Theme(
      json.id, 
      json.title
    );
  }
}