<script lang="ts">
    let {
        onSave,
        onCancel,
    }: {
        onSave: (title: string, content: string) => void;
        onCancel: () => void;
    } = $props();

    let title = $state("");
    let content = $state("");
    let showError = $state(false);

    function submit() {
        if (!title.trim()) {
            showError = true;
            return;
        }
        onSave(title.trim(), content);
    }
</script>

<div class="form">
    <div class="field">
        <label for="doc-title">Title</label>
        <input
            id="doc-title"
            type="text"
            placeholder="Document title"
            bind:value={title}
            oninput={() => (showError = false)}
        />
        {#if showError}
            <p class="field-error">A title is required.</p>
        {/if}
    </div>
    <div class="field field-grow">
        <label for="doc-content">Text</label>
        <textarea
            id="doc-content"
            placeholder="Paste or write the document text..."
            bind:value={content}
        ></textarea>
    </div>
    <div class="actions">
        <button class="btn-secondary" onclick={onCancel}>Cancel</button>
        <button class="btn-primary" onclick={submit}>Add document</button>
    </div>
</div>

<style>
    .form {
        display: flex;
        flex-direction: column;
        height: 100%;
        padding: 20px 24px;
        gap: 14px;
    }

    .field {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .field-grow {
        flex: 1;
        min-height: 0;
    }

    label {
        font-size: 12px;
        font-weight: 600;
        color: var(--color-text-muted);
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }

    input,
    textarea {
        font-family: inherit;
        font-size: 13.5px;
        color: var(--color-text);
        background: var(--color-surface);
        border: 1px solid var(--color-border);
        border-radius: 6px;
        padding: 8px 10px;
        outline: none;
    }

    input:focus,
    textarea:focus {
        border-color: var(--color-accent);
    }

    textarea {
        flex: 1;
        min-height: 0;
        resize: none;
        line-height: 1.5;
    }

    .field-error {
        margin: 0;
        font-size: 12px;
        color: #dc2626;
    }

    .actions {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
        flex-shrink: 0;
    }

    button {
        padding: 7px 16px;
        font-size: 13px;
        font-weight: 500;
        border-radius: 6px;
        border: none;
        cursor: pointer;
        transition: opacity 0.1s;
        font-family: inherit;
    }

    button:hover {
        opacity: 0.85;
    }

    .btn-primary {
        background: var(--color-accent);
        color: #fff;
    }

    .btn-secondary {
        background: var(--color-surface);
        color: var(--color-text);
        border: 1px solid var(--color-border);
    }
</style>
