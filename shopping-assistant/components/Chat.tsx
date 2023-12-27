"use client";

import Image from "next/image";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Send } from "lucide-react";

const messages = [
  {
    type: "bot",
    text: "Hello, how can I help you?",
  },
  {
    type: "user",
    text: "I want to buy a smartphone",
  },
  {
    type: "bot",
    text: "What brand?",
  },
  {
    type: "user",
    text: "Apple",
  },
  {
    type: "bot",
    text: "What model?",
  },
  {
    type: "user",
    text: "iPhone 12",
  },
  {
    type: "bot",
    text: "Here are some options",
  },
];

const Chat = () => {
  return (
    <section>
      <h2 className="flex gap-4 rounded-t-md border border-primary bg-secondary px-4 py-2 text-2xl font-semibold text-primary">
        <Image src="/chat-logo.svg" alt="logo" width={32} height={32} />
        Personal Shopper
      </h2>
      <ScrollArea className="h-96 rounded-b-md border border-primary">
        {messages.map((message, index) => (
          <ChatMessage message={message} key={index} />
        ))}
      </ScrollArea>
      <div className="grid grid-cols-[1fr_auto] items-center gap-2 py-2">
        <Input type="search" placeholder="Search" className="h-12" />
        <Button
          type="submit"
          className="m-0 aspect-square h-12 p-2"
          onClick={() => console.log("search")}
        >
          <Send className="h-4 w-4" />
        </Button>
      </div>
    </section>
  );
};

const ChatMessage = ({
  message: { type, text },
}: {
  message: { type: string; text: string };
}) => {
  switch (type) {
    case "user":
      return (
        <div className="mx2 mx-2 my-4 flex items-center justify-start gap-2">
          <div className="rounded-md bg-primary p-2 text-white">
            <p>{text}</p>
          </div>
        </div>
      );
    case "bot":
      return (
        <div className="mx-4 my-4 flex items-center justify-end gap-2">
          <div className="rounded-md bg-neutral-100 p-2">
            <p>{text}</p>
          </div>
        </div>
      );
    default:
      return null;
  }
};

export default Chat;
