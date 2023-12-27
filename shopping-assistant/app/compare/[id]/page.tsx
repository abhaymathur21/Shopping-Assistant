"use client";

import { products } from "@/data/products.json";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { Product } from "@/components/Products";
import { Button } from "@/components/ui/button";
import Link from "next/link";

const ComparePage = ({ params: { id } }: { params: { id: number } }) => {
  const product = products.find((product) => product.id === +id);
  const router = useRouter();

  if (!product) {
    router.push("/");
    return null;
  }
  const {
    title,
    description,
    price,
    discountPercentage,
    rating,
    stock,
    brand,
    category,
    thumbnail,
    images,
    source,
  } = product;

  return (
    <div className="grid max-h-[32rem] gap-8 overflow-y-auto px-4">
      <div className="grid">
        <div className="flex h-64 w-64 flex-col items-center justify-center place-self-center">
          <Image
            src={thumbnail}
            alt={title}
            className="h-full w-full object-cover"
            height={500}
            width={500}
          />
        </div>
        <div>
          <h1 className="text-3xl font-bold">{title}</h1>
          <p className="mb-4 text-sm font-bold text-gray-400">
            {brand} | {category}
          </p>
          {discountPercentage ? (
            <div className="mb-4 flex items-center">
              <p className="text-2xl font-bold text-primary">
                £{(price * (1 - discountPercentage / 100)).toFixed(2)}
              </p>
              <p className="ml-4 text-xl font-bold text-gray-400 line-through">
                £{price}
              </p>
            </div>
          ) : (
            <p className="text-2xl font-bold text-red-600">£{price}</p>
          )}

          <p className="mb-4 text-xl font-bold text-gray-400">
            Rating {rating} / 5
          </p>

          <p className="text-muted-foreground">{description}</p>

          {images.length > 0 && (
            <div className="mt-4 grid grid-cols-4 gap-4">
              {images.map((image) => (
                <Image
                  key={image}
                  src={image}
                  alt={title}
                  className="h-32 w-32 object-contain"
                  height={128}
                  width={128}
                />
              ))}
            </div>
          )}

          <p className="text-xl font-bold text-gray-400">
            Source:{" "}
            {source === "A" ? (
              <Button variant="link">
                <Link href="amazon.com">Amazon</Link>
              </Button>
            ) : (
              <Button variant="link">
                <Link href="ebay.com">eBay</Link>
              </Button>
            )}
          </p>

          <Button
            className="w-full"
            variant="default"
            onClick={() => console.log("add to cart")}
          >
            Add to cart
          </Button>
        </div>
      </div>
    </div>
  );
};

const ProductCompareView = ({ id }: { id: number }) => {
  return (
    <div>
      <h1>Compare Prices</h1>
      <p>Product ID: {id}</p>
    </div>
  );
};

export default ComparePage;
