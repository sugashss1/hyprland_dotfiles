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
