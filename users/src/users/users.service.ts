import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

import { createHash } from 'crypto';

import { User } from './entities/user.entity';

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private _usersRepository: Repository<User>
  ) {}

  hashPassword(password: string): string {
    return createHash('sha512').update(password).digest('hex');
  }

  findId(id: number): Promise<User | undefined > {
    return this._usersRepository.findOne({ id });
  }

  findOne(username: string): Promise<User | undefined> {
    return this._usersRepository.findOne({ username });
  }

  findByAuth(username: string, password: string): Promise<User | undefined> {
    return this._usersRepository.findOne({
      username,
      password: this.hashPassword(password)
    });
  }

  async create(username: string, password: string, email: string): Promise<string> {
    const userWithUsername = await this.findOne(username);

    if (userWithUsername) {
      return "login unavailable";
    }

    const userWithEmail = await this._usersRepository.findOne({ email });

    if (userWithEmail) {
      return "email unavailable";
    }

    const user = new User();
    user.username = username;
    user.password = this.hashPassword(password);
    user.email = email;
    user.joinDate = (new Date()).getTime();
    user.lastDate = (new Date()).getTime();

    await this._usersRepository.save([user]);

    return "";
  }
}
