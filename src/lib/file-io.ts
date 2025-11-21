import { save } from '@tauri-apps/plugin-dialog';
export const filePath = await save({
  filters: [{
    name: 'Image',
    extensions: ['json']
  }]
});