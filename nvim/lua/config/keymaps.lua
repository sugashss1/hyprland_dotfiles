-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
--
--
vim.keymap.set("x", "d", '"_d', { desc = "Delete without yanking" })
vim.keymap.set({ "n", "t" }, "<C-/>", function()
  Snacks.terminal.toggle("/usr/bin/fish", {
    win = {
      split = "below",
      position = "bottom",
    },
  })
end, { desc = "Terminal (CWD)" })

local function set_snippet_jump(direction, key)
  vim.keymap.set({ "i", "s" }, key, function()
    if vim.snippet.active({ direction = direction }) then
      return string.format("<Cmd>lua vim.snippet.jump(%d)<CR>", direction)
    else
      return key
    end
  end, {
    desc = "vim.snippet.jump if active, otherwise " .. key,
    expr = true,
    silent = true,
  })
end

set_snippet_jump(-1, "<C-H>")
set_snippet_jump(1, "<C-l>")
