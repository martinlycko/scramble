#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[derive(serde::Serialize, serde::Deserialize)]
struct ProjectData {
    name: String,
    created_at: String,
    #[serde(default)]
    sources: Vec<serde_json::Value>,
    #[serde(default)]
    codes: Vec<serde_json::Value>,
    #[serde(default)]
    folders: Vec<serde_json::Value>,
}

#[tauri::command]
fn create_project(path: String, name: String, created_at: String) -> Result<ProjectData, String> {
    let data = ProjectData {
        name,
        created_at,
        sources: vec![],
        codes: vec![],
        folders: vec![],
    };
    let json = serde_json::to_string_pretty(&data).map_err(|e| e.to_string())?;
    std::fs::write(&path, json).map_err(|e| e.to_string())?;
    Ok(data)
}

#[tauri::command]
fn open_project(path: String) -> Result<ProjectData, String> {
    let contents = std::fs::read_to_string(&path).map_err(|e| e.to_string())?;
    serde_json::from_str(&contents).map_err(|e| e.to_string())
}

#[tauri::command]
fn save_project(path: String, data: ProjectData) -> Result<(), String> {
    let json = serde_json::to_string_pretty(&data).map_err(|e| e.to_string())?;
    std::fs::write(&path, json).map_err(|e| e.to_string())?;
    Ok(())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![
            greet,
            create_project,
            open_project,
            save_project
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
